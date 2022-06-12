using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000039: Namid
/// </summary>
public class _11000039 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:0831180407000204$
    // - Who will protect $map:02000051$?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407000208$
                // - Sometimes you get what you want. Sometimes you must settle.
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
