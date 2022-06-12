using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001437: Dilton
/// </summary>
public class _11001437 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1219225907005431$
    // - This is bad! The stream that runs through our village is drying out.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1219225907005434$
                // - We built the village around the stream. It keeps us alive in the inhospitable desert.
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
