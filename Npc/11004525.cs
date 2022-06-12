using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004525: Timid Soldieretto
/// </summary>
public class _11004525 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0103163407012506$
    // - Beeep... Beeep...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0103163407012507$
                // - Beep... Beep... Beep...
                return 10;
            case (10, 1):
                // $script:0103163407012508$
                // - Beep... Beep... Beeep! Bee...
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
