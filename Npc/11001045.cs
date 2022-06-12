using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001045: Rauter
/// </summary>
public class _11001045 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003569$
    // - What just passed by? It was shining.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003572$
                // - Experience really is the best teacher. I've worked at this research center for so long that now I know scientific terms better than slang.
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
