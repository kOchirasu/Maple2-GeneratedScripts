using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001396: Navila
/// </summary>
public class _11001396 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40;50
    }

    // Select 0:
    // $script:1217193307005396$
    // - What's wrong?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1226235907005592$
                // - The ruins... These diseases... They all broke out around... No, the timeline doesn't fit.
                switch (selection) {
                    // $script:1226235907005593$
                    // - What are you mumbling about?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1226235907005594$
                // - Ah, yes? Can I help you?
                switch (selection) {
                    // $script:1226235907005595$
                    // - You look like you've got a lot on your mind.
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:1226235907005596$
                // - Yes, you're right. I'm trying to figure some things out. And you're interrupting me.
                switch (selection) {
                    // $script:1226235907005597$
                    // - Oops! I didn't mean to.
                    case 0:
                        return 33;
                }
                return -1;
            case (33, 0):
                // $script:1226235907005598$
                // - Good.
                return -1;
            case (40, 0):
                // $script:1227015507005608$
                // - This is all my fault...
                return -1;
            case (50, 0):
                // $script:0201104007005866$
                // - I won't be so arrogant or impatient ever again. I'll try to be careful from now on. Thank you for your help, $MyPCName$.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.SelectableDistractor,
            (33, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
