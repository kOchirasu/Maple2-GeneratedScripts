using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001696: 
/// </summary>
public class _11001696 : NpcScript {
    protected override void FirstScript() {
        (Id, Button) = (30, NpcTalkButton.SelectableDistractor);
    }

    protected override (int, NpcTalkButton) Next(int selection) {
        switch (Id) {
            case 0:
                // $script:0707174810001589$ 
                // - You look a bit on edge. Why not let your hair down and have a drink at the Penguin Bar?
                return default;
            case 30:
                // $script:0707174810001590$ 
                // - How'd you like to use a Golden Bell Ticket? It's a chance to buy a round of drinks for people at the Penguin Bar!
                switch (selection) {
                    // $script:0707174810001591$
                    // - Buy it for 1,000,000 mesos.
                    case 0:
                        // TODO: goto 31
                        // (Id, Button) = (31, NpcTalkButton.Close);
                        // TODO: gotoFail 32
                        // (Id, Button) = (32, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                }
                return default;
            case 31:
                // $script:0707174810001592$ functionID=1 
                // - <font color="#ffd200">$MyPCName$</font>, what a fine, fine person you are! Thanks to you, everyone will get a free drink! Just ring the golden bell next to you.
                return default;
            case 32:
                // $script:0707174810001593$ 
                // - It's <font color="#ffd200">1,000,000 mesos</font> for a Golden Bell Ticket.
                //   Do you not have enough mesos? Then I'm sorry, you can't ring the bell.
                return default;
        }
        
        return default;
    }
}
