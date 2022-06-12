using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003063: Surmany
/// </summary>
public class _11003063 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:0102155907007646$
    // - What do you want?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0102155907007647$
                // - You must conserve your energy in the cold. That's why I don't talk much. Just so you know. 
                return -1;
            case (40, 0):
                // $script:0207083707007919$
                // - Oh look, it's $MyPCName$ the worrywart. What do you want?
                switch (selection) {
                    // $script:0207083707007920$
                    // - I need burning breaths!
                    case 0:
                        return 41;
                    // $script:0207083707007921$
                    // - Why are you so much smaller than the other snowfolks?
                    case 1:
                        return 42;
                }
                return -1;
            case (41, 0):
                // functionID=1 openTalkReward=True 
                // $script:0207083707007922$
                // - There you go. This is because you got those materials for me, you know. Helping others pays off!
                return -1;
            case (42, 0):
                // $script:0207083707007923$
                // - Excuse me? Hey, that's none of your business! And I'm not small... the others are just really big!
                //   <font color="#909090">(He's gotten sulky. I don't think he'll want to talk to me anymore.)</font>
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Close,
            (42, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
