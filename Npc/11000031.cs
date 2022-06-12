using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000031: Asimov
/// </summary>
public class _11000031 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0831180407000181$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407000182$
                // - The power of the Green Lapenta is especially strong here in $map:02000023$. That vital force protects this place from darkness.
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
