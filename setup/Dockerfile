FROM ubuntu:18.04

# install dependencies
RUN apt-get update
RUN apt-get install -y \
	build-essential \
	git \
	python-pip \
	python2.7 \
	python2.7-dev \
	cmake \
	libusb-1.0.0 \
	libusb-1.0-0.dev \
	usbutils \
	kmod \
	initramfs-tools \
	&& apt-get autoremove \
	&& apt-get clean

# updating pip
RUN pip install --upgrade pip

# installing rtl-sdr driver
WORKDIR /usr/local/
RUN git clone git://git.osmocom.org/rtl-sdr.git
RUN mkdir /usr/local/rtl-sdr/build
WORKDIR /usr/local/rtl-sdr/build
RUN cmake ../ -DINSTALL_UDEV_RULES=ON -DDETACH_KERNEL_DRIVER=ON
RUN make
RUN make install
WORKDIR "/"
RUN udevadm control --reload
RUN udevadm trigger

RUN echo "blacklist dvb_usb_rtl28xxu" >> /etc/modprobe.d/rtl-sdr-blacklist.conf
RUN echo "blacklist e4000" >> /etc/modprobe.d/rtl-sdr-blacklist.conf
RUN echo "blacklist rtl2832" >> /etc/modprobe.d/rtl-sdr-blacklist.conf
RUN ldconfig
RUN update-initramfs -u


# install PyBOMBS
#RUN pip install PyBOMBS

# configure PyBOMBS
#RUN pybombs auto-config
#RUN pybombs -y recipes add-defaults
#RUN pybombs -y recipes add gr-recipes https://github.com/gnuradio/gr-recipes.git
#RUN pybombs -y recipes add gr-etcetera https://github.com/gnuradio/gr-etcetera.git
#RUN pybombs prefix init ~/prefix -a default -R gnuradio-default

# installing modules
#RUN pybombs install gr-lte
