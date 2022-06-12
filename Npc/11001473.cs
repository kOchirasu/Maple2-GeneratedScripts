using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001473: Kovin
/// </summary>
public class _11001473 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1224110207005582$
    // - What brings you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1228134707005720$
                // - Nothing is more precious than the ruins and artifacts that our ancestors have left behind. Today, I'm especially proud to be an archaeologist!
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
