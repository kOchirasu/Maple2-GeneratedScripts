using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001382: Zendal
/// </summary>
public class _11001382 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1217193307005382$
    // - What brings you here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1228164407005727$
                // - If you're thinking of investing in $map:02010036$, you're too late... friend. I was here first.
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
