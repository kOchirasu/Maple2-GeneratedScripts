using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004530: Reika
/// </summary>
public class _11004530 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;50
    }

    protected override int Select() {
        // Select 0:
        // $script:0103163407012522$
        // - I see you there.
        // Select 40:
        // $script:0104140207012582$
        // - I can't stand the noise here...
        // TODO: 0,40
        return 0;
    }

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0103163407012523$
                // - Can I help you?
                switch (selection) {
                    // $script:0103163407012524$
                    // - I'm just checking in on things.
                    case 0:
                        return 20;
                }
                return -1;
            case (20, 0):
                // $script:0103163407012525$
                // - $npcName:11004437[gender:0]$ sent you, then. As you can see, nothing's changed.
                return 20;
            case (20, 1):
                // $script:0103163407012526$
                // - We're still getting shot at by wild robots. We're still dealing with these ridiculous dust clouds. And we're still getting motion sickness when that machine over there sends out tremors...
                return 20;
            case (20, 2):
                // $script:0103163407012527$
                // - I miss the forest.
                return 20;
            case (20, 3):
                // $script:0103163407012528$
                // - ...
                return 20;
            case (20, 4):
                // $script:0103163407012529$
                // - When you get back to the outpost, let them know we need reinforcements to help with the killer machines here.
                switch (selection) {
                    // $script:0103163407012530$
                    // - Will do.
                    case 0:
                        return 30;
                }
                return -1;
            case (30, 0):
                // $script:0103163407012531$
                // - Thanks. You're a life saver!
                return -1;
            case (50, 0):
                // $script:0104140207012583$
                // - The dust here is unreal... I should have brought a face mask.
                return 50;
            case (50, 1):
                // $script:0104140207012584$
                // - I'm going to get a lung disease from my time in this place. Hopefully it's all just in my head...
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (20, 0) => NpcTalkButton.Next,
            (20, 1) => NpcTalkButton.Next,
            (20, 2) => NpcTalkButton.Next,
            (20, 3) => NpcTalkButton.Next,
            (20, 4) => NpcTalkButton.SelectableDistractor,
            (30, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.Next,
            (50, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
