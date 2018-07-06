#会計を求める                                                               
  2 #値段                                                                       
  3 beer_v = 200                                                                
  4 otumami_v = 100                                                             
  5 yakitori_v = 100                                                            
  6 #個数                                                                       
  7 beer_c = 2                                                                  
  8 otumami_c = 1                                                               
  9 yakitori_c = 2                                                              
 10 #割引                                                                       
 11 rate = 0.8                                                                  
 12 point = 150                                                                 
 13 # 計算                                                                      
 14 sum_v = (beer_v * beer_c) + (otumami_v * otumami_c) + (yakitori_v * yakitori    _c)                                                                         
 15 payment = ((beer_v * beer_c) + (otumami_v * otumami_c) + ((yakitori_v * rate    ) * yakitori_c)) - (point)                                                  
 16                                                                             
 17 # 結果を表示                                                                
 18 print("買い物の合計は", sum_v, "円")                                        
 19 print("割引してもらうと", payment, "円")  
