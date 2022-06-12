using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004742: 
/// </summary>
public class _11004742 : NpcScript {
    protected override void FirstScript() {
        // TODO: RandomPick 30;40
        // (Id, Button) = (30, NpcTalkButton.SelectableDistractor);
        // (Id, Button) = (40, NpcTalkButton.Next);
    }

    protected override (int, NpcTalkButton) Next(int selection) {
        switch (Id) {
            case 0:
                // $script:1024162710002270$ 
                // - Spin $npc:11004742$ for just 1 $item:30001446$!
                return default;
            case 30:
                // $script:1024162710002271$ functionID=1 
                // - Give us 2 $itemPlural:30001446$ for a chance to spin the $npc:11004742$. How about it? Feeling lucky?
                switch (selection) {
                    // $script:1024162710002272$
                    // - (Pay 2 $item:30001446$ for 1 spin.)
                    case 0:
                        // TODO: goto 31
                        // (Id, Button) = (31, NpcTalkButton.Next);
                        // TODO: gotoFail 32
                        // (Id, Button) = (32, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                    // $script:1024162710002273$
                    // - (Pay 20 $itemPlural:30001446$ for a bunch of spins in a row!)
                    case 1:
                        // TODO: goto 10
                        // (Id, Button) = (10, NpcTalkButton.Next);
                        // TODO: gotoFail 32
                        // (Id, Button) = (32, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                    // $script:1024162710002274$
                    // - (Pay 200 $itemPlural:30001446$ for a bunch of spins in a row!)
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
                        // $script:1024162710002275$ functionID=1 buttonSet=16 
                        // - Wonderful! Are you ready to spin?
                        return (31, NpcTalkButton.Close);
                    case 1:
                        // $script:1024162710002276$ buttonSet=1 
                        // - Here's hoping Lady Luck's on your side!
                        return default;
                }
                break;
            case 32:
                // $script:1024162710002277$ functionID=1 
                // - You don't have enough coins. You need 2 $itemPlural:30001446$ to spin the $npc:11004742$ once.
                return default;
            case 40:
                switch (Index++) {
                    case 0:
                        // $script:1024162710002278$ functionID=1 
                        // - You need 2 $itemPlural:30001446$ to give the $npc:11004742$ a spin. Play Hide-and-Seek to get $itemPlural:30001446$!
                        return (40, NpcTalkButton.Close);
                    case 1:
                        // $script:1024162710002279$ 
                        // - If you have $itemPlural:30001446$ to burn, be sure to come to $map:02000064$!
                        return default;
                }
                break;
            case 10:
                switch (Index++) {
                    case 0:
                        // $script:1024162710002280$ functionID=1 buttonSet=16 
                        // - All right, let's spin it 10 times in a row! Keep your fingers crossed, $MyPCName$!
                        return (10, NpcTalkButton.Close);
                    case 1:
                        // $script:1024162710002281$ buttonSet=17 
                        // - Spin number $rouletteCurrent$! Good luck!
                        return default;
                }
                break;
            case 100:
                switch (Index++) {
                    case 0:
                        // $script:1024162710002282$ functionID=1 buttonSet=16 
                        // - All right, let's spin it 100 times in a row! Keep your fingers crossed, $MyPCName$!
                        return (100, NpcTalkButton.Close);
                    case 1:
                        // $script:1024162710002283$ buttonSet=17 
                        // - Spin number $rouletteCurrent$! Good luck!
                        return default;
                }
                break;
        }
        
        return default;
    }
}
