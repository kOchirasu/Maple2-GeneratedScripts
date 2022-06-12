using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001553: Lusoy
/// </summary>
public class _11001553 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:0415104107006019$
    // - What brings you here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0421104907006039$
                // - Are you here to fish? This place is wonderful. I came here with my sister, Bory, and we're having a blast!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
