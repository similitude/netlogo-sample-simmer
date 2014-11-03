/**
 * The API for the NetLogo models.
 */

service NetLogoService {

  /**
   * Invokes NetLogo from the command line.
   */
  string call(1:map<string, string> clargs)

  /**
   * Runs the evolutionary Altruism simulation.
   * See http://ccl.northwestern.edu/netlogo/models/Altruism
   */
  string altruism(
    1:double altruisticProbability,
    2:double selfishProbability,
    3:double altruismCost,
    4:double altruismBenefit,
    5:double disease,
    6:double harshness,
    7:i32 numTicks
  )
  
  // TODO: Termination conditions, interactive sampling, etc.

  // TODO: Other models.

}
