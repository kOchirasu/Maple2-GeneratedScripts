using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003138: 
/// </summary>
public class _11003138 : NpcScript {
    protected override void FirstScript() {
        // TODO: RandomPick 30;40
        // (Id, Button) = (30, NpcTalkButton.SelectableDistractor);
        // (Id, Button) = (40, NpcTalkButton.Next);
    }

    protected override (int, NpcTalkButton) Next(int selection) {
        switch (Id) {
            case 30:
                // $script:0212230610001824$ 
                // - Welcome!
                //   Pay me 3 $itemPlural:30000745$, and I'll let you spin $npc:11003138$.
                //   How about it? Feeling lucky?
                switch (selection) {
                    // $script:0212230610001825$
                    // - Pay 3 $itemPlural:30000745$ to spin once.
                    case 0:
                        // TODO: goto 31
                        // (Id, Button) = (31, NpcTalkButton.Next);
                        // TODO: gotoFail 32
                        // (Id, Button) = (32, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                    // $script:0212230610001826$
                    // - Pay 30 $itemPlural:30000745$ to spin 10 times.
                    case 1:
                        // TODO: goto 10
                        // (Id, Button) = (10, NpcTalkButton.Next);
                        // TODO: gotoFail 32
                        // (Id, Button) = (32, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                    // $script:0212230610001827$
                    // - Pay 300 $itemPlural:30000745$ to spin 100 times.
                    case 2:
                        // TODO: goto 100
                        // (Id, Button) = (100, NpcTalkButton.Next);
                        // TODO: gotoFail 32
                        // (Id, Button) = (32, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                }
                return default;
            case 31:
                switch (Index++) {
                    case 0:
                        // $script:0212230610001828$ functionID=1 buttonSet=16 
                        // - Spin the wheel for a chance at great prizes! You know you want to.
                        return (31, NpcTalkButton.Close);
                    case 1:
                        // $script:0212230610001829$ buttonSet=1 
                        // - Here's hoping Lady Luck's on your side!
                        return default;
                }
                break;
            case 32:
                // $script:0212230610001830$ 
                // - It seems like you're a little short. You need 3 $itemPlural:30000745$ to spin the $npc:11003138$.
                return default;
            case 40:
                switch (Index++) {
                    case 0:
                        // $script:0212230610001831$ 
                        // - To take a spin on the $npc:11003138$, you need 3 $itemPlural:30000745$. But there's good news! Starting April 25th, you can get 3 $itemPlural:30000745$ in your Mailbox once per day, right when you first log in! You'll also get bonus coins based on your cumulative playtime. As if that weren't enough, even more coins will be given to you if you join any of the various events we're hosting!
                        return (40, NpcTalkButton.Close);
                    case 1:
                        // $script:0212230610001832$ 
                        // - If you have $itemPlural:30000745$ to burn, be sure to come to $map:02000360$!
                        return default;
                }
                break;
            case 10:
                switch (Index++) {
                    case 0:
                        // $script:0212230610001833$ functionID=1 buttonSet=16 
                        // - All right, let's spin it 10 times in a row! Keep your fingers crossed, $MyPCName$!
                        return (10, NpcTalkButton.Close);
                    case 1:
                        // $script:0212230610001834$ buttonSet=17 
                        // - Roulette spin number $rouletteCurrent$! Good luck!
                        return default;
                }
                break;
            case 100:
                switch (Index++) {
                    case 0:
                        // $script:0212230610001835$ functionID=1 buttonSet=16 
                        // - All right, let's spin it 100 times in a row! Keep your fingers crossed, $MyPCName$!
                        return (100, NpcTalkButton.Close);
                    case 1:
                        // $script:0212230610001836$ buttonSet=17 
                        // - Roulette spin number $rouletteCurrent$! Good luck!
                        return default;
                }
                break;
        }
        
        return default;
    }
}
