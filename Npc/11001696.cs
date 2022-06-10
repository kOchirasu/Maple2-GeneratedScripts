using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001696: 
/// </summary>
public class _11001696 : NpcScript {
    internal _11001696(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0707174810001589$ 
                // - You look a bit on edge. Why not let your hair down and have a drink at the Penguin Bar?
                return true;
            case 30:
                // $script:0707174810001590$ 
                // - How'd you like to use a Golden Bell Ticket? It's a chance to buy a round of drinks for people at the Penguin Bar!
                switch (selection) {
                    // $script:0707174810001591$
                    // - Buy it for 1,000,000 mesos.
                    case 0:
                        Id = 0; // TODO: 31 | 32
                        return false;
                }
                return true;
            case 31:
                // $script:0707174810001592$ functionID=1 
                // - <font color="#ffd200">$MyPCName$</font>, what a fine, fine person you are! Thanks to you, everyone will get a free drink! Just ring the golden bell next to you.
                return true;
            case 32:
                // $script:0707174810001593$ 
                // - It's <font color="#ffd200">1,000,000 mesos</font> for a Golden Bell Ticket.
                //   Do you not have enough mesos? Then I'm sorry, you can't ring the bell.
                return true;
            default:
                return true;
        }
    }
}
