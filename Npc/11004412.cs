using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004412: Mason
/// </summary>
public class _11004412 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1113161307011841$
    // - It is time my order stood with the rest of the empire.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1113161307011842$
                // - Whatever challenges this new land has in store for us, let them come. I will show them my true power.
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
