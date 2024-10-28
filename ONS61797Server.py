"""
Copyright (c) 2024 NF Corporation

Permission is hereby granted, free of charge, to any person obtaining a copy of 
this software and associated documentation files (the "Software"), to deal in 
the Software without restriction, including without limitation the rights to use, 
copy, modify, merge, publish, distribute, sublicense, and/or sell copies of 
the Software, and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS 
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN 
AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION 
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from ONS61797 import ONS61797
from labrad.server import LabradServer, setting


class ONS61797Server(LabradServer):
    """
    A server for controlling the ONS61797 device through Labrad.

    Attributes
    ----------
    device : ONS61797 or None
        Instance of the ONS61797 device or None if not connected.

    Methods
    -------
    connect(c, port, ip_address)
        Connects to the ONS61797 device using the provided port and IP address.

    close(c)
        Closes the connection to the device and sets the device attribute to None.

    on(c, channel)
        Turns on the specified channel of the device.

    off(c, channel)
        Turns off the specified channel of the device.

    get_output_state(c, channel)
        Returns the output state (on/off) of the specified channel.

    set_voltage(c, channel, voltage)
        Sets the voltage of the specified channel.

    get_voltage(c, channel)
        Returns the current voltage of the specified channel.

    get_device_information(c)
        Returns the device information as a string.

    reset(c)
        Resets the device.

    set_ip_address(c, ip_address)
        Sets the IP address of the device.

    get_ip_address(c)
        Returns the IP address of the device.

    set_subnet_mask(c, subnet_mask)
        Sets the subnet mask of the device.

    get_subnet_mask(c)
        Returns the subnet mask of the device.

    set_default_gateway(c, default_gateway)
        Sets the default gateway of the device.

    get_default_gateway(c)
        Returns the default gateway of the device.
    """

    name = "ONS61797 Server"

    def __init__(self):
        """
        Initializes the ONS61797Server instance.
        """
        super(ONS61797Server, self).__init__()
        self.device = None

    def __del__(self):
        """
        Ensures that the device connection is closed when the server is deleted.
        """
        if self.device:
            self.device.close()

    @setting(10, "Connect", port="s", ip_address="s")
    def connect(self, c, port, ip_address):
        """
        Connect to the ONS61797 device.

        Parameters
        ----------
        c : context
            The context for this setting call.
        port : str
            The port to connect to the device.
        ip_address : str
            The IP address of the device.
        """
        self.device = ONS61797(port=port, ip_address=ip_address)

    @setting(11, "Close")
    def close(self, c):
        """
        Close the connection to the ONS61797 device.

        Parameters
        ----------
        c : context
            The context for this setting call.
        """
        self.device.close()
        self.device = None

    @setting(12, "On", channel="i")
    def on(self, c, channel):
        """
        Turn on the specified channel.

        Parameters
        ----------
        c : context
            The context for this setting call.
        channel : int
            The channel number to turn on.
        """
        self.device.on(channel=channel)

    @setting(13, "Off", channel="i")
    def off(self, c, channel):
        """
        Turn off the specified channel.

        Parameters
        ----------
        c : context
            The context for this setting call.
        channel : int
            The channel number to turn off.
        """
        self.device.off(channel=channel)

    @setting(14, "Get Output State", channel="i")
    def get_output_state(self, c, channel):
        """
        Get the output state of the specified channel.

        Parameters
        ----------
        c : context
            The context for this setting call.
        channel : int
            The channel number to query.

        Returns
        -------
        bool
            The output state of the channel (True if on, False if off).
        """
        return self.device.get_output_state(channel=channel)

    @setting(15, "Set Voltage", channel="i", voltage="v")
    def set_voltage(self, c, channel, voltage):
        """
        Set the voltage of the specified channel.

        Parameters
        ----------
        c : context
            The context for this setting call.
        channel : int
            The channel number to set the voltage.
        voltage : float
            The voltage to set for the channel.
        """
        self.device.set_voltage(channel=channel, voltage=voltage)

    @setting(16, "Get Voltage", channel="i", returns="v")
    def get_voltage(self, c, channel):
        """
        Get the voltage of the specified channel.

        Parameters
        ----------
        c : context
            The context for this setting call.
        channel : int
            The channel number to query.

        Returns
        -------
        float
            The current voltage of the specified channel.
        """
        return self.device.get_voltage(channel=channel)

    @setting(17, "Get Device Information", returns="s")
    def get_device_information(self, c):
        """
        Get information about the device.

        Parameters
        ----------
        c : context
            The context for this setting call.

        Returns
        -------
        str
            The device information as a string.
        """
        return self.device.get_device_information()

    @setting(18, "Reset Device")
    def reset(self, c):
        """
        Reset the device.

        Parameters
        ----------
        c : context
            The context for this setting call.
        """
        self.device.reset()

    @setting(19, "Set IP Address", ip_address="s")
    def set_ip_address(self, c, ip_address):
        """
        Set the IP address of the device.

        Parameters
        ----------
        c : context
            The context for this setting call.
        ip_address : str
            The new IP address for the device.
        """
        self.device.set_ip_address(ip_address=ip_address)

    @setting(20, "Get IP Address", returns="s")
    def get_ip_address(self, c):
        """
        Get the current IP address of the device.

        Parameters
        ----------
        c : context
            The context for this setting call.

        Returns
        -------
        str
            The current IP address of the device.
        """
        return self.device.get_ip_address()

    @setting(21, "Set Subnet Mask", subnet_mask="s")
    def set_subnet_mask(self, c, subnet_mask):
        """
        Set the subnet mask of the device.

        Parameters
        ----------
        c : context
            The context for this setting call.
        subnet_mask : str
            The new subnet mask for the device.
        """
        self.device.set_subnet_mask(subnet_mask=subnet_mask)

    @setting(22, "Get Subnet Mask", returns="s")
    def get_subnet_mask(self, c):
        """
        Get the current subnet mask of the device.

        Parameters
        ----------
        c : context
            The context for this setting call.

        Returns
        -------
        str
            The current subnet mask of the device.
        """
        return self.device.get_subnet_mask()

    @setting(23, "Set Default Gateway", default_gateway="s")
    def set_default_gateway(self, c, default_gateway):
        """
        Set the default gateway of the device.

        Parameters
        ----------
        c : context
            The context for this setting call.
        default_gateway : str
            The new default gateway for the device.
        """
        self.device.set_default_gateway(default_gateway=default_gateway)

    @setting(24, "Get Default Gateway", returns="s")
    def get_default_gateway(self, c):
        """
        Get the current default gateway of the device.

        Parameters
        ----------
        c : context
            The context for this setting call.

        Returns
        -------
        str
            The current default gateway of the device.
        """
        return self.device.get_default_gateway()


__server__ = ONS61797Server()


if __name__ == "__main__":
    from labrad import util

    util.runServer(__server__)
