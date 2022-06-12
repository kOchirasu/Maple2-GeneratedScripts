using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000741: Bevento
/// </summary>
public class _11000741 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407002883$
    // - What? I'm in the middle of creating music that speaks to the soul!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407002885$
                // - Sigh... Do you even know the pain of creation? Bah, there's no soul in this music. If there was, I'd be able to feel it!
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
