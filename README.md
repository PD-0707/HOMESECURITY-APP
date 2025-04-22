# HOMESECURITY-APP
Abstract

This paper presents an innovative home security system that integrates Internet of Things (IoT) technology with advanced Artificial Intelligence (AI) techniques to achieve real-time intrusion detection, face recognition, and suspicious behaviour analysis. The proposed system employs a multi-sensor architecture including Passive Infrared (PIR) sensors, magnetic door sensors, and Raspberrypi3 with camera module to trigger image capture and video streaming. A lightweight LBPH-based face recognition model, supplemented by Open Pose-based suspicious behaviour detection, enables the system to distinguish authorized from unauthorized entries and escalate alerts in a tiered manner. The proposed method significantly reduces false alarms and enhances response times compared to conventional security systems.


Introduction

Recent increases in residential security breaches necessitate the evolution of conventional alarm systems. Traditional methods, which primarily rely on simple motion detection, suffer from high false positive rates and lack contextual awareness. In contrast, IoT-based solutions have begun to incorporate multiple sensor modalities; however, many of these systems function in isolation and do not effectively combine sensor data with AI-driven analysis. This paper introduces a comprehensive home security solution that fuses sensor-triggered image capture with advanced face recognition and behaviour analysis. 


Literature Survey

[1] The literature on IoT-based smart home security systems emphasizes the use of biometric authentication methods, such as face recognition (via HAAR classifiers) and fingerprint sensors (e.g., R307), to enhance security. Additionally, IoT integration with platforms like ESP32 and Arduino enables remote monitoring and control of security features through mobile applications. Machine learning algorithms, including CNNs and motion detection techniques, are utilized for real-time threat detection and system optimization.

[2] This review paper examines the growing prevalence of smart-home security systems enabled by the Internet of Things (IoT). The authors highlight the various security threats inherent in IoT ecosystems such as unauthorized access, data breaches, and device tampering. The paper delves into current security mechanisms like encryption, authentication, and intrusion detection and explores potential improvements in device authentication, user education, and the development of robust security standards.

[3] This paper presents a home security system using Arduino UNO microcontroller for door lock control. The system incorporates two-level security passwords and is connected to the homeowner's mobile via GSM module, allowing remote access. In case of unauthorized access, the system sends alerts to the homeowner for verification. The paper discusses the feasibility of using solenoid locks for physical security along with the advantages of integrating IoT for remote monitoring.

[4] This paper describes the development of a Home Security Application using Android Studio, enabling real-time video surveillance, door/window sensors, motion detection, alarm control, and remote access. The system allows users to interact with the security system via a user-friendly interface, providing remote control for various security devices such as security cameras and door locks. The application offers integration with other smart home devices and enhances the overall security experience by sending instant notifications in case of any breaches. It also supports data analysis to help users track incidents and improve security patterns.


Proposed Methodology

Sensor Data Acquisition and Integration

The system’s hardware layer integrates multiple sensors. The PIR sensor strategically placed around the premises to cover critical entry points. When any sensor is activated, an interrupt signal is sent to the Arduino Uno, which then commands the Raspberry pi Camera module to capture and stream images. The magnetic door sensor provides an additional layer of security by detecting physical tampering with entry points.

AI-Based Face Recognition

The LBPH face recognition model is employed due to its efficiency and low computational overhead, which is ideal for embedded systems. Captured images are pre-processed (converted to grayscale, resized, and normalized) before feature extraction. The model then compares these features against a database of authorized individuals. If the prediction confidence is below a predefined threshold, the subject is classified as “Unknown.”

Suspicious Behaviour Detection

Following the detection of an unknown face, the system activates Open Pose to analyse body posture and movement. By monitoring key points such as the head, shoulders, and limbs, the system determines if the behaviour deviates from normal patterns (e.g., loitering, abrupt changes, or unusual poses). This multi-tiered approach ensures that the system not only reacts to simple motion but also understands the context, thereby minimizing false alarms.

Emergency Protocol

The software layer is designed to escalate alerts based on the severity of sensor activations; a warning message is sent to the user’s mobile application.


Results and Discussion

Our proposed system demonstrates a significant improvement over traditional security systems by integrating multiple sensor modalities with AI-driven analysis. The use of the LBPH algorithm ensures rapid face recognition, while Open Pose contributes to accurate behaviour detection. However, challenges remain in calibrating sensor thresholds and ensuring robust performance under various environmental conditions. Future work will focus on optimizing these parameters and exploring the integration of additional sensors to further enhance detection accuracy.


Conclusion

This report presented a comprehensive IoT-based home security system that employs a layered sensor architecture coupled with AI for face recognition and suspicious activity detection. The system’s novel integration of PIR, and magnetic door sensors with a Raspberry pi and a real-time emergency protocol provides a robust solution to modern home security challenges. Future work will involve extensive field testing, integration of additional AI models for improved behaviour analysis, and the exploration of multi-camera setups to enhance system coverage and introducing escalation protocol.


References

[1] Peddarapu Ramakrishna, M. Vandana, K. Sachin, S. Sai Vignesh, Irfan Ahmad Rather, "Smart Home Security System Using IoT", International Journal of Engineering Research & Technology (IJERT), Volume 12, Issue 4, April 2023.

[2] George Vardakis, George Hatzivasilis, Eleftheria Koutsaki, and Nikos Papadakis, "Review of Smart-Home Security Using the Internet of Things", Electronics, Volume 13, Issue 16, Article 3343, August 2024.

[3] Aman Sharma, Anjana Goen, "Smart Home Security System", International Journal of Electronics and Communication Engineering, Volume 9, Issue 3, Pages 120-125, 2023.

[4] Joshi Sarvesh, R. Latha, "Home Security Application Using Android Studio", International Research Journal of Modernization in Engineering Technology and Science (IRJMETS), Volume 5, Issue 7, July 2023, Pages 2203-2210,

