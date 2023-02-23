# 네모네모 고등학교 졸업식  
## Description
네모네모 고등학교 졸업식은 사용자로부터 받은 이미지를 픽셀 캐릭터로 변환시켜주는 프로젝트입니다. 각종 api와 딥러닝 모델을 통해 원본 사진에서 표정, 얼굴 비율, 얼굴과 머리 색상, 머리 스타일, 안경 유무 등을 파악하여 다양한 캐릭터를 만들 수 있습니다. 
## Tools
 - <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white"/>
 - <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=white"/>
 - <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white"/>
 - <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=PyTorch&logoColor=white"/>
 - <img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=white"/>
 - <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
 -  <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=HTML5&logoColor=white"/>
 

## Models
| 기준 | 모델 | 분류 |
|--|--|--|
| 헤어 스타일 | EfficientNet | 11((웨이브)긴머리, (웨이브)단발머리, (웨이브)숏컷, 포니테일, 양갈래, 양갈래, 땋은머리, 대머리)  |
| 앞머리 스타일 | shufflenet v2 | 4(덮은 머리, 깐머리, 반깐머리, 가르마 머리) |
| 안경 | Mobilenet v2 | 2 |
| 표정 | Naver api(face recognition) | 5(기본, 슬픔, 기쁨, 무표정, 신남) |
| 얼굴 비율 | Naver api(face recognition) | 3 |
| 색상 | Naver api(face recognition) | 얼굴: 9, 헤어: 추출된 색상 |

## Prototype

![캡처](https://user-images.githubusercontent.com/89053845/219292003-f3501e10-e1bc-4cf3-887a-6e79addb311d.PNG)

## Files
중요 파일 간단히 설명

## Prerequisite
미리 설치해야 할 패키지, 의존성이 걸리는 문제 작성
### Packages
asgiref==3.6.0  
certifi==2022.12.7  
charset-normalizer==3.0.1  
Django==4.1.5  
django-cleanup==6.0.0  
django-social-share==2.3.0  
idna==3.4  
numpy==1.24.1  
opencv-python==4.7.0.68  
Pillow==9.4.0  
requests==2.28.2  
sqlparse==0.4.3  
torch==1.13.1  
torchvision==0.14.1  
typing_extensions==4.4.0  
urllib3==1.26.14

## Usages
어떻게 사용하면 되는지에 대한 설명
