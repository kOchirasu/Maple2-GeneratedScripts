using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001841: Joddy
/// </summary>
public class _11001841 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1020165907007306$
    // - Ohhh... Ugh... I'm okay...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1020165907007307$
                // - Aw man. I really don't think that went super great. Why can't I be more like you?
                switch (selection) {
                    // $script:1111015907007384$
                    // - Maybe you need to take a break.
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1020165907007308$
                // - Jeez, you think so? See, here I was thinking I gotta train harder. Otherwise, I'll never get strong enough to help you...
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
