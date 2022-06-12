using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000376: Timmy
/// </summary>
public class _11000376 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407001544$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407001547$
                // - Do you believe in aliens? I do! There has to be loads of intelligent creatures out there, the universe is huge! You should stop by some night and watch the stars with me.
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
