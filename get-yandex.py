import urllib2, re
# example: <dd class='value m_temp c'>+9<span class="meas">&deg;C</span></dd>
page = urllib2.urlopen('http://pogoda.yandex.ru/omsk/?ncrnd=6724').read()
string_pos = page.find('b-thermometer__now')
temperature = page[string_pos+20:string_pos+30]
temperature = temperature[:temperature.find(' ')];
temperature = temperature.replace('+','').replace('&minus;','-')
print temperature
