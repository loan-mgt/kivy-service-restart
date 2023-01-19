# kivy-service-restart
I am trying to build a rudimentary app with Kivy on android to understand the fundamentals of service.

I am trying to make my **service restart**, but I didn't succeed.

the service work but doesn’t restart
the code doesn't give an error
Does someone know what I did wrong?

[link to stackoverflow question](https://stackoverflow.com/questions/65859554/kivy-service-wont-restart-autorestart)


**the architecture of my file:**
 
              -buildozer.spec
              -scr
                |-> main.py
                |-> service.py


### Log
ActivityManager: Process org.kivy.oscservice:service_Pong (pid 27830) has died: svc SVC 

01-30 23:55:00.012  1315  4034 I ActivityManager: Process org.kivy.oscservice:service_Pong (pid 29178) has died: svcb SVC 
01-30 23:55:00.012  1315  4034 W ActivityManager: Scheduling restart of crashed service org.kivy.oscservice/.ServicePong in 1000ms
01-30 23:55:01.041  1315  1471 I ActivityManager: Start proc 29428:org.kivy.oscservice:service_Pong/u0a165 for service org.kivy.oscservice/.ServicePong
01-30 23:55:01.169 29428 29428 E AndroidRuntime: Process: org.kivy.oscservice:service_Pong, PID: 29428
01-30 23:55:01.169 29428 29428 E AndroidRuntime: java.lang.RuntimeException: Unable to start service org.kivy.oscservice.ServicePong@ae87b11 with null: java.lang.NullPointerException: Attempt to invoke virtual method 'android.os.Bundle android.content.Intent.getExtras()' on a null object reference

