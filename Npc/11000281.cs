using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000281: Konadu
/// </summary>
public class _11000281 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407001095$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407001097$
                // - You see that guard over there? I'm telling you, no respect for scholars or history. He keeps harassing me for researching instead of sticking to his own tasks. He has no idea... 
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
