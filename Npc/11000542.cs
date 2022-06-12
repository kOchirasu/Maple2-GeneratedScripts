using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000542: Tanz
/// </summary>
public class _11000542 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407002311$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407002313$
                // - If you're not happy with your life, you should dance. When your body's happy, your mind will be too!
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
