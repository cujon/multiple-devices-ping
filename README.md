# multiple-devices-ping
Ping multiple devices and execute system command.

This is script is able to ping two devices and only if both of these devices are not responding, then the system command is executed.

The while loop runs forever or until both variables fail1 and fail2 reaches a count of 10 (or more).
address1 and address2 are being pinged every one minute. If the response code is not 0 then the fail counter increments by one. A response of 0 means success.

Works with both Linux and Windows
For Windows I was only able to make it work with IPv6 adresses.

# Contributions
Ideas for improvements are welcome.
