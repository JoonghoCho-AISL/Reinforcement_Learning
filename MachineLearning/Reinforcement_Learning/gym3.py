import gym
# Create simulation instance
env = gym.make('BipedalWalker-v3')
# 학습 과정은 에피소드로 구분
# 새로운 에피소드가 시작되면 환경을 초기화
for i_episode in range(100):
    observation = env.reset()
    # 환경 렌더링
    for i in range(10000):
        env.render()
        print(observation)
        # 에이전트가 취할 수 있는 행동들의 집합인 행동공간에서
        # 무작위로 임의의 행동을 선택
        action = env.action_space.sample()
        #행동을 할 때 마다 observation, reward, done, Info 변수 기록
        observation, reward, done, info = env.step(action)
        '''
        observation은 환경의 관찰을 나타내는 객체
        reward는 이전 행동으로부터 얻은 보상
        done은 참 거짓을 나타내는 bool 형식의 값 (에피소드의 완료를 유무 저장)
        info는 디버깅에 유용한 정보
        '''
        #done이 True 일 때, 에피소드에서 얻은 타임 스텦을 출력하고 에피소드 중단
        if done:
            print("{} timesteps taken for the Episode".format(i+1))
            break
