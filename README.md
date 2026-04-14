# My Deep Learning Practice Codes

## 1. Hotel_Booking_Data_EDA_prac

 목표 : 데이터 셋을 분석해 호텔 예약 취소에 영향을 주는 요인들에는 무엇이 있는지 찾아보기
 활용 데이터셋 : Kaggle의 Hotel Booking Demand Datasets

 데이터 시각화(히트맵, 산점도 그래프, 피벗테이블)등 여러 column을 비교하며 예약 취소에 어떤 요인이 큰 영향을 주는지 찾아보는 연습을 하였다.

 블로그 주소 : 
 
 https://uj07096.tistory.com/2  
 https://uj07096.tistory.com/3
<br><br><br>



## 2. Bank_Marketing_Data_EDA_prac

목표 : 포르투갈 은행의 마케팅 데이터를 분석하고, 분류 모델을 구축하여 마케팅 캠페인의 효율성을 높이는 전략을 도출
활용 데이터셋 : 2008~2010년까지의 포르투갈 은행 마케팅 캠페인 데이터(UC Irvine Machine Learning Repository 제공)


LogitricRegression, SVM, RandomForest, GradientBoosting, HistGradientBoosting 모델을 활용해 예측을 진행하고, SHAP 분석을 통해 어떤 column이 영향을 많이 주는지 분석해보고 결론을 도출해보는 연습을 진행했다.

블로그 주소 :   
https://uj07096.tistory.com/20  
https://uj07096.tistory.com/21
<br><br><br>


## 3. denoising_prac

목표 : 손상된 문서를 복원, 노이즈를 제거하여 원본 문서를 최대한 복원하는 것(AutoEncoder 활용)
활용 데이터셋 : Kaggle의 Denoising Dirty Documents

직접 간단한 AutoEncoder을 만들어서 노이즈가 있는 이미지 데이터를 복원하는 작업을 진행했다. 손실함수를 관찰하며 하이퍼파라미터 튜닝을 진행했고, 테스트 파일에 대해서 성공적으로 복원에 성공했다.

블로그 주소 : https://uj07096.tistory.com/39
<br><br><br>



## 4. Air_Pollution_Forecast_LSTM

목표 : LSTM을 활용해 pollution 수치 예측, 시계열 데이터 올바르게 전처리하기
활용 데이터셋 : Kaggle의 Air Pollution Forecasting - LSTM Multivariation

LSTM을 불러와 Optuna를 이용한 베이지안 하이퍼파라미터 튜닝을 진행했었는데, 시간이 오래걸리는 문제가 발생하여 Early Stopping, pruning 등등 시간 감소에 도움되는 기법들을 많이 시도해보았다.

블로그 주소 :  
https://uj07096.tistory.com/40  
https://uj07096.tistory.com/41
<br><br><br>


## 5. fine_tuning_prac

목표 : 흉부 X-Ray 사진을 바탕으로 폐렴 환자 구분, Transfer Learning을 통해 분류 모델 구축
활용 데이터셋 : Kaggle의 Chest X-Ray Images (Pneumonia)

사전학습 되어있는 ResNEt, EfficientNet, DenseNet, ConvNeXt 모델을 불러와 모델에 대한 성능 테스트를 Feature Extraction하여 먼저 진행하였고, 상위 2개 성능지표를 보인 모델에 미세조정을 하여 X-Ray 분류를 진행하였고, Layer-Cam을 활용하여 모델이 어디에 집중하여 분류를 하였는지 시각화하였다.

블로그 주소 :   
https://uj07096.tistory.com/49  
https://uj07096.tistory.com/50
<br><br><br>

## 6. Object_Detection_prac
목표 : SSD모델을 활용하여 강아지와 고양이의 얼굴을 감지하는 Detection 작업 수행
활용 데이터셋 : Kaggle의 The Oxford-IIIT Pet Dataset

Kaggle에서 강아지와 고양이 이미지 데이터를 받아와, Faster R-CNN, SSD, YOLO 모델을 가져와 학습시켜 강아지와 고양이의 얼굴을 감지하는 Object Detection 작업을 수행했고, 성능지표 비교와 test 데이터에 대한 결과 시각화를 했다. YOLO 모델이 가장 간편하게 사용가능하기도 하고, mAP도 높게 나와 왜 실무에서 현재 객체인식 분야에서 많이 사용되는지 알 수 있었다.

블로그 주소 :   
https://uj07096.tistory.com/52  
https://uj07096.tistory.com/53
<br><br><br>


## 7. Sementic_Segmentation_Football_Dataset
목표 : U-Net을 이용해 축구 경기 영상 내의 다양한 객체(예: 골대, 심판, 선수, 관중 등)를 픽셀 단위로 분할하는 Semantic Segmentation 작업을 수행했다. Custom한 U-Net과 ResNet 백본 교체를 한 모델을 비교하여 backbone의 유무효과를 비교했고, 또한 backbone의 weights인자를 이용해 사전학습 유무의 효과도 비교하였다.
활용 데이터셋 : Kaggle의 Football (Semantic Segmentation) Dataset

블로그 주소 :
https://uj07096.tistory.com/65
https://uj07096.tistory.com/66