using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001305: Manovich
/// </summary>
public class _11001305 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1215203907005024$
    // - $MyPCName$, what is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1228222807005746$
                // - No wonder the empress was in such a hurry to see me. It's always something... 
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
