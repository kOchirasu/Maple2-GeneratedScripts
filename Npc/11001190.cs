using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001190: Blackstar Gangster
/// </summary>
public class _11001190 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1015162707004157$
    // - What brings you here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1015162707004160$
                // - Trying to steal a Blackstar train? They've got to be crazy!
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
