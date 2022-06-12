using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001167: Brynn
/// </summary>
public class _11001167 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1008163207004079$
    // - Where in the world is he?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1008163207004082$
                // - Have you seen my brother? He must be somewhere around here.
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
