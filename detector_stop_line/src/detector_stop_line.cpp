#include <string>

// Include ROS
#include "ros/console.h"
#include "ros/ros.h"
#include "detector_stop_line/stop_line_msg.h"
#include "sensor_msgs/Image.h"
const std::string NODE_NAME = "detector_stop_line";
const std::string SUB_TOPIC = "usb_cam/image_raw";
const std::string PUB_TOPIC = "stop_line_data";
const std::string WINDOW_TITLE = "Camera";


constexpr int ESC_KEY = 27;
constexpr int WIDTH = 640;
constexpr int HEIGHT = 480;

// Include OpenCV
#include "opencv2/opencv.hpp"

class Detect {
  ros::NodeHandle node;
  ros::Subscriber sub;
  ros::Publisher pub;
  cv::Mat vFrame;
  bool stop_line_flag;
  int count;
public:
  Detect()
    : 
      stop_line_flag(false) {
    sub = node.subscribe(SUB_TOPIC, 1, &Detect::callback, this);
    pub = node.advertise<detector_stop_line::stop_line_msg>(PUB_TOPIC, 1);
    cv::namedWindow(WINDOW_TITLE);
  }
  
  void callback(const sensor_msgs::ImageConstPtr& msg);
  void process();
  void publish();
  void publish2();
};

void Detect::callback(const sensor_msgs::ImageConstPtr& msg) {
  try {
    this->vFrame = cv::Mat(HEIGHT, WIDTH, CV_8UC3,
                           const_cast<uchar*>(&msg->data[0]), msg->step);
    this->process();
  } catch (const std::exception& e) {
    ROS_ERROR("callback exception: %s", e.what());
    return;
  }
}

void Detect::process(){
  cv::cvtColor(this->vFrame, this->vFrame, cv::COLOR_BGR2RGB);

  cv::Mat gray_image;
  cv::cvtColor(this->vFrame,gray_image, cv::COLOR_RGB2GRAY);

  cv::Mat blur_image;
  cv::GaussianBlur(gray_image, blur_image, cv::Size(5, 5), 2);

  cv::Mat canny_image;
  cv::Canny(blur_image, canny_image, 50, 150);
  cv::Mat roi = canny_image(cv::Rect(100, 370, 440, 50));
  std::vector<cv::Vec4i> all_lines;
  cv::HoughLinesP(roi,
      all_lines,
      1.0,
      CV_PI / 180.0,
      40,
      40,
      5);
  if (all_lines.size() >= 0){
    count = 0;
    for(size_t i = 0 ; i <all_lines.size(); i++){
      cv::Vec4i l = all_lines[i];
      if (abs(l[1]-l[3]) < 10)
        line(this->vFrame, cv::Point(l[0] +100, l[1]+370), cv::Point(l[2]+100, l[3]+370), cv::Scalar(0,0,255), 3, cv::LINE_AA);
        count++;
    }
  }
  if (count >= 4)
    this->publish();
  else 
    this->publish2();


  cv::imshow(WINDOW_TITLE, this->vFrame);
  cv::imshow("Test", roi);

  

}

void Detect::publish(){
  detector_stop_line::stop_line_msg msg;
  msg.header.stamp = ros::Time::now();
  msg.header.frame_id = PUB_TOPIC;
  msg.stop_line_flag = true;

  this->pub.publish(msg);
}

void Detect::publish2(){
  detector_stop_line::stop_line_msg msg;
  msg.header.stamp = ros::Time::now();
  msg.header.frame_id = PUB_TOPIC;
  msg.stop_line_flag = false;

  this->pub.publish(msg);
}

int main(int argc, char** argv) {
  ros::init(argc, argv, NODE_NAME);
  Detect detect;
  while (ros::ok()) {
    ros::spinOnce();
    int k = cv::waitKey(1);
    if (k == ESC_KEY || k == ' ') break;
  }
  cv::destroyAllWindows();
  return 0;
}