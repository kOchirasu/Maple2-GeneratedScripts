using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004470: Colorata
/// </summary>
public class _11004470 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1227195007012417$
    // - I was playing hide-and-seek with my friends, but I just can't find them!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1227195007012418$
                // - I was playing hide-and-seek with my friends, but I just can't find them!
                return 10;
            case (10, 1):
                // $script:1227195007012419$
                // - Where did you go?! I give up! Please come out!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
