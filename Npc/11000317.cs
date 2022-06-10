using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000317: Jonn
/// </summary>
public class _11000317 : NpcScript {
    internal _11000317(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001205$ 
                // - What is it?
                return true;
            case 40:
                // $script:0831180407001209$ 
                // - Ah, are you an adventurer? So am I!
                switch (selection) {
                    // $script:0831180407001210$
                    // - Don't you lie to me!
                    case 0:
                        Id = 41;
                        return false;
                    // $script:0831180407001211$
                    // - What is an adventurer to you?
                    case 1:
                        Id = 42;
                        return false;
                }
                return true;
            case 41:
                // $script:0831180407001212$ 
                // - I-I'm not lying! I mean it!
                switch (selection) {
                    // $script:0831180407001213$
                    // - What do you think an adventurer is?
                    case 0:
                        Id = 42;
                        return false;
                }
                return true;
            case 42:
                // $script:0831180407001214$ 
                // - An adventurer is someone who embarks on adventures around the world! I've even been to $map:02000023$, you know. My next destination is $map:02000051$!
                return true;
            default:
                return true;
        }
    }
}
