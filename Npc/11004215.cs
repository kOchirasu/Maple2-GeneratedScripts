using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004215: Stellar Chest
/// </summary>
public class _11004215 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;50
    }

    // Select 0:
    // $script:0808172007010849$
    // - <font color="#909090">(This $npcName:11004215$ can create gem dust to help you upgrade your gemstones.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0808172007010850$
                // - <font color="#909090">(Do you wish to create some $itemPlural:20301849$?)</font>
                switch (selection) {
                    // $script:0808172007010851$
                    // - (Create 1.)
                    case 0:
                        // TODO: goto 11
                        // TODO: gotoFail 14
                        return 14;
                    // $script:0808172007010852$
                    // - (Create 10.)
                    case 1:
                        // TODO: goto 21
                        // TODO: gotoFail 24
                        return 24;
                    // $script:0808172007010853$
                    // - (Not now.)
                    case 2:
                        return 15;
                }
                return -1;
            case (11, 0):
                // $script:0808172007010854$
                // - <font color="#909090">(Consume 10 $itemPlural:30001187$ and 1 $item:30001188$ to make 1 $item:20301849$?)</font> 
                switch (selection) {
                    // $script:0808172007010855$
                    // - (Create 1 $item:20301849$.)
                    case 0:
                        // TODO: goto 12
                        // TODO: gotoFail 13
                        return 13;
                }
                return -1;
            case (12, 0):
                // functionID=1 openTalkReward=True 
                // $script:0808172007010856$
                // - <font color="#909090">(The process has been completed. The chest awaits your next command.)</font> 
                return -1;
            case (13, 0):
                // $script:0808172007010860$
                // - <font color="#909090">(Your bag is full. Return after making some space.)</font>
                return -1;
            case (14, 0):
                // $script:0808172007010861$
                // - <font color="#909090">(Insufficient materials. You need 10 $itemPlural:30001187$ and 1 $item:30001188$ to begin the conversion process.)</font>
                return -1;
            case (15, 0):
                // $script:0808172007010862$
                // - <font color="#909090">(The cube stands by.)</font>
                return -1;
            case (21, 0):
                // $script:0808172007010857$
                // - <font color="#909090">(Consume 100 $itemPlural:30001187$ and 10 $itemPlural:30001188$ to make 10 $itemPlural:20301849$?)</font> 
                switch (selection) {
                    // $script:0808172007010858$
                    // - (Create 10 $itemPlural:20301849$.)
                    case 0:
                        // TODO: goto 22
                        // TODO: gotoFail 13
                        return 13;
                }
                return -1;
            case (22, 0):
                // functionID=2 openTalkReward=True 
                // $script:0808172007010859$
                // - <font color="#909090">(The process has been completed. The chest awaits your next command.)</font> 
                return -1;
            case (24, 0):
                // $script:0809135407010882$
                // - <font color="#909090">(Insufficient materials. You need 100 $itemPlural:30001187$ and 10 $itemPlural:30001188$ to begin the conversion process.)</font>
                return -1;
            case (50, 0):
                // $script:0911140307011157$
                // - <font color="#909090">(After you reach level 50, you can use $itemPlural:30001187$ and $itemPlural:30001188$ on this chest to make materials for upgrading gemstones.)</font>
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.Close,
            (13, 0) => NpcTalkButton.Close,
            (14, 0) => NpcTalkButton.Close,
            (15, 0) => NpcTalkButton.Close,
            (21, 0) => NpcTalkButton.SelectableDistractor,
            (22, 0) => NpcTalkButton.Close,
            (24, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
