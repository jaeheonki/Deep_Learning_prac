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
목표 : U-Net을 이용해 축구 경기 영상 내의 다양한 객체(예: 골대, 심판, 선수, 관중 등)를 픽셀 단위로 분할하는 Semantic Segmentation 작업을 수행   
활용 데이터셋 : Kaggle의 Football (Semantic Segmentation) Dataset  


Custom한 U-Net과 ResNet 백본 교체를 한 모델을 비교하여 backbone의 유무효과를 비교했고, 또한 backbone의 weights인자를 이용해 사전학습 유무의 효과도 비교하였다.

블로그 주소 :  
https://uj07096.tistory.com/65  
https://uj07096.tistory.com/66
<br><br><br>


## 8. GAN_Diffusion_prac
목표 : 모델을 활용하여 FashionMNIST 데이터셋의 각 패션 아이템(예: 티셔츠, 바지, 스니커즈 등)을 조건부로 생성하는 작업을 수행  
활용 데이터셋 : FashionMINST 데이터셋

각 클래스에 해당하는 이미지를 생성하는 cGAN모델과, 추가로 Diffusion(LDM) 모델을 직접 설계하여(VAE, Time-Embedding, Latent U-Net, DDPM) 조건 추가 하는 방식을 One-Hot과 Embedding 방식을 비교하여 성능지표를 실험했고, 결과 이미지를 시각화는 것 까지 수행했다.  


블로그 주소 :   
https://uj07096.tistory.com/69  
https://uj07096.tistory.com/70
<br><br><br>

## 9. GRU_text_classification
목표 : 텍스트 데이터를 입력으로 받아 뉴스의 카테고리를 예측하는 딥러닝 모델 구현  
활용 데이터셋 : 활용 데이터셋 : sklearn.dataset의 fetch_20newsgroups 데이터셋  

GRU, Bi-GRU, Bi-GRU+Attention 세 모델을 비교하며 20 Newsgroups 데이터셋으로 텍스트 분류를 수행하고, Optuna 및 Layer Normalization, 불용어 처리 등 다양한 방법으로 하이퍼파라미터 튜닝을 진행했다.  



블로그 주소 :  
https://uj07096.tistory.com/81  
https://uj07096.tistory.com/82  
<br><br><br>

## 10. Seq2Seq_Transformer_Translation
목표 : 한국어 문장을 영어로 번역하는 Seq2Seq + Attention, Transformer 모델을 직접 구현하고 성능 비교  
활용 데이터셋 : 일상생활 및 구어체 한영 데이터셋 (코드잇 제공, Train 120만 / Val 15만 쌍)  

GRU 기반 Seq2Seq + Bahdanau Attention 모델과 직접 구현한 Transformer 모델을 비교하여 한→영 기계번역 태스크를 수행했다. SentencePiece BPE 토크나이저를 한국어/영어 각각 별도로 학습시켰고, BLEU Score로 성능을 평가한 결과 Seq2Seq 0.1075, Transformer 0.2304로 Transformer가 더 자연스러운 번역 성능을 보였다.  


블로그 주소 :  
https://uj07096.tistory.com/89  
<br><br><br>

## 11. BERT_GPT_Document_Summarization
목표 : PyTorch로 BERT(MLM+SOP 사전학습)와 GPT 언어 모델을 직접 구현하고 한국어 문서로 사전학습 수행  
활용 데이터셋 : 코드잇 제공 한국어 뉴스 문서 요약 데이터셋 (Train 320,961개 / Val 39,298개)  

KLUE-BERT 토크나이저를 활용해 BERT와 GPT를 처음부터 직접 구현하여 사전학습했다. BERT는 Segment Embedding 누락과 MLM/SOP 손실 스케일 불균형 문제를 디버깅하며 개선했고, GPT는 Greedy Decoding의 반복 패턴 문제를 Top-k + Temperature Sampling으로 완화했다. 최종 성능은 BERT MLM Perplexity 1,292 / SOP Accuracy 0.5084, GPT Perplexity 270 / BLEU 0.0322로, 소규모 데이터 학습의 한계를 실험적으로 확인했다.  


블로그 주소 :  
https://uj07096.tistory.com/93
https://uj07096.tistory.com/94  
<br><br><br>
