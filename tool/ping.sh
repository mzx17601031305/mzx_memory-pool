#!/bin/bash
echo 开始时间：`date` >>/tmp/pingdate.txt	//记录此脚本执行一次周期时间
for ip in $(cat /Users/mazixuan/Desktop/mzx_memory-pool/tool/ip_list.txt|sed "/^#/d")		//读取本地待ping主机列表文件
  do
     ping -c 1 $ip &>/dev/null
     a=$?
     sleep 2
     #ping -c 1 $ip &>/dev/null
     #b=$?
     #sleep 2
     #ping -c 1 $ip &>/dev/null
     #c=$?
     #sleep 2
     DATE=$(date +%F" "%H:%M)
     if [ $a -ne 0 -a $a -ne 0 -a $a -ne 0 ];then


     #if [ $a -ne 0 -a $b -ne 0 -a $c -ne 0 ];then	//如需3次ping取值会更准确，但是耗时加倍
        echo `date` 这台设备PING不通了，主机DOWN了或网络出现闪断故障 | mail -s "$ip" 17601031305@163.com  //多个邮件接收人用逗号隔开
     fi
done
echo 结束时间：`date` >>/tmp/pingdate.txt
