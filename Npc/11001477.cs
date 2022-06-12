using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001477: Blackstar Gangster
/// </summary>
public class _11001477 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:1228113207005717$
    // - What brings you here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:1228113207005719$
                // - Those weren't ordinary train robbers.
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
