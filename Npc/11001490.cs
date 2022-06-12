using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001490: Ereve
/// </summary>
public class _11001490 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0114152507005802$
    // - $MyPCName$, what brings you to me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0114152507005804$
                // - It was no small task to recover the power of light. I pray it will never be overshadowed by darkness.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
