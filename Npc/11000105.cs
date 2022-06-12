using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000105: Benhurst
/// </summary>
public class _11000105 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407000429$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000432$
                // - Honey, if you're looking to make a splash in $map:02000001$'s social scene, you're gonna need to do something about that outfit.
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
