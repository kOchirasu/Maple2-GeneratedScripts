using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004501: Drill Sergeant
/// </summary>
public class _11004501 : NpcScript {
    internal _11004501(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1227192907012407$ 
                // - You here to enlist? Fall in line, Recruit! 
                return true;
            case 10:
                // $script:1227192907012408$ 
                // - You here to enlist? Fall in line, Recruit! 
                switch (selection) {
                    // $script:1227192907012409$
                    // - I'm not your recruit.
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1227192907012410$ 
                // - Is that so? Hmph. You have the look of a washed-up loser. Join my troop and I'll have you back on your feet in no time! 
                // $script:1227192907012411$ 
                // - We need all the help we can get to fight Tairen. We'll even take folks wearing... whatever that's supposed to be. You sure you don't want to sign on with us? 
                switch (selection) {
                    // $script:1227192907012412$
                    // - I'll think about it...
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:1227192907012413$ 
                // - Whenever and wherever, we're ready! 
                return true;
            default:
                return true;
        }
    }
}
