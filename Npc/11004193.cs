using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004193: Landevian
/// </summary>
public class _11004193 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0813101707010954$
    // - What...?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0813101707010955$
                // - What happened? I'm having trouble remembering.
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
