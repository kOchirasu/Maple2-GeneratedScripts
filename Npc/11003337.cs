using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003337: Dark Wind Commander
/// </summary>
public class _11003337 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0510143807008461$
    // - I will protect the lives of my men... No matter what...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0510145607008465$
                // - Dark Wind doesn't give up so easily!
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
