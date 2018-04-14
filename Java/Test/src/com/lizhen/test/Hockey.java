//ÎÄ¼şÃû: Hockey.java
package com.lizhen.test;

public interface Hockey extends Sports
{
	public void homeGoalScored();
	public void visitingGoalScored();
	public void endOfPeriod(int period);
	public void overtimePeriod(int ot);
}
