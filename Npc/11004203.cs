using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004203: Tourist
/// </summary>
public class _11004203 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010654$
    // - It's a pleasure.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010655$
                // - It's a bit hot out here, but spectating is such fun!
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
