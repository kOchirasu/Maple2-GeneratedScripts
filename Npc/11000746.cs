using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000746: Rakael
/// </summary>
public class _11000746 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407002938$
    // - <b>Chomp! Snarf!</b>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002941$
                // - Not all witches are greedy and evil. I've been studying useful spells to help $map:02000023$.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
