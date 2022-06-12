using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004537: Barricade Defender
/// </summary>
public class _11004537 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0104170807012611$
    // - We're doing our best to defend $map:02020041$!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0104170807012612$
                // - We're doing our best to defend $map:02020041$!
                return 10;
            case (10, 1):
                // $script:0104170807012613$
                // - Send me to where the fighting's thickest! I'll crush any enemy in my path!
                return 10;
            case (10, 2):
                // $script:0104170807012614$
                // - Umm... Would you mind taking a few of them out while you're here? N-not that I can't take them myself, of course!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Next,
            (10, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
