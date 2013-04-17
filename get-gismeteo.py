import urllib2, re
# example: <dd class='value m_temp c'>+9<span class="meas">&deg;C</span></dd>
page = urllib2.urlopen('http://www.gismeteo.ru/city/daily/4578/').read(60000)
string_pos = page.find('m_temp c');
temperature = page[string_pos+10:string_pos+20];
temperature = temperature[:temperature.find('<')];
temperature = temperature.replace('+','').replace('&minus;','-')
print temperature
