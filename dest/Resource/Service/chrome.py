B
    A��^�  �               @   s�   d dl Z d dlmZmZ d dlZd dlZdZdd� Zedkr�xFe�	e�
� �D ]4\ZZZx(eD ] Zed  dkr\ej�de � q\W qLW e �� Ze�e� � dS )	�    N)�connect�launchz�() =>
           Object.defineProperties(navigator,{
             webdriver:{
               get: () => false
             }
           })

c           	   �   s�   ddl m}  | � }|�� }|�� }|�� }tddgd�I d H }tdd��}|�|j� W d Q R X |�	� I d H }|d }|�
|�I d H  |�t�I d H  |�d| d	 | �I d H  t�d
�I d H  |�� I d H  |�� I d H  d S )Nr   )�ConfigTz--no-sandbox)Zheadless�argsZws�wzhttp://�:i -1)ZResource.config_dir.configr   Zget_service_ip_addressZget_service_port_numberZget_service_useragentr   �open�writeZ
wsEndpointZpagesZsetUserAgentZevaluate�webdriver_jsZgoto�asyncioZsleep�close)r   ZconfigZipZportZuaZbrowser�fZpage� r   �.\Resource\Service\chrome.py�connect_chrome   s     r   �__main__�_z%s)r   Zpyppeteer.launcherr   r   �sys�osr
   r   �__name__�walk�getcwd�root�dirs�files�d�path�appendZget_event_loopZloopZrun_until_completer   r   r   r   �<module>   s   
