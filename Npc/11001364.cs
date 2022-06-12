using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001364: Tara
/// </summary>
public class _11001364 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1215222907005047$
    // - All of us here, together... It reminds me of the old days.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1230171207005754$
                // - Okay, I admit it. You're a good person. I can't always be right, you know. Anyway, thank you for the help.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
